from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from guardapp.validators import guard_id_validator, guard_gender_validator
from residentapp.validators import resident_id_validator

# from .utils import get_a_token
from .validators import guest_id_validator, token_validator

__models__ = [
    'Human',
    'Block',
    'Resident',
    'Guard',
    'Token',
    'Guest',
    'Record',
    'Issue',
    'Bill',
]


# validators here due to circular import
def fill_length(word: str, length_be: int, fill_by: str):
    if len(fill_by) != 1:
        raise AttributeError('Length of fill_by must be 1.')
    return f'{fill_by}' * (length_be - len(word)) + word


def get_a_token():
    now = timezone.now()
    year = fill_length(str(now.year), 4, '0')
    month = fill_length(str(now.month), 2, '0')
    day = fill_length(str(now.day), 2, '0')
    hour = fill_length(str(now.hour), 2, '0')
    minute = fill_length(str(now.minute), 2, '0')
    second = fill_length(str(now.second), 2, '0')
    token = hex(int(year + month + day + hour + minute + second))[2:].upper()

    return token


def who_id_validator(given_id: str):
    if not (given_id.startswith('RS-') or given_id.startswith('GS-') or given_id.startswith('GA-')):
        raise ValidationError("Human ID must start with RS (if resident) or GS (if guest) or GA (if guard)")
    if given_id.startswith('RS-'):
        try:
            Resident.objects.get(resident_id__exact=given_id)
        except Resident.DoesNotExist:
            raise ValidationError("No resident exists with this id.")
    elif given_id.startswith('GS-'):
        try:
            Guest.objects.get(guest_id__exact=given_id)
        except Guest.DoesNotExist:
            raise ValidationError("Not a valid guest id. Entry request denied.")


# models
class Human(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    UNKNOWN = 'unknown'

    GENDER_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
        (OTHER, 'other'),
        (UNKNOWN, 'unknown')
    ]
    last_index = len(GENDER_CHOICES) - 1
    lar_gender_len = max(len(g[0]) for g in GENDER_CHOICES)

    user = models.OneToOneField(User, models.CASCADE, related_name='the_human')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=lar_gender_len, default=UNKNOWN)
    nid_or_br = models.CharField(verbose_name='National identity card or Birth registration No.', max_length=20)
    contact = models.CharField(verbose_name='Phone number', max_length=11)
    date_of_birth = models.DateField('Date of Birth')
    photo = models.ImageField(upload_to='human')

    def __str__(self):
        return self.user.get_username()

    class Meta:
        verbose_name_plural = 'Human'


class Block(models.Model):
    # ordinal numbers
    FLOORS = [
        ('Ground', 'Ground'),
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
        ('9th', '9th'),
        ('10th', '10th'),
    ]
    BLOCK_LABELS = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    name = models.CharField(choices=BLOCK_LABELS, max_length=1, default='A')
    floor = models.CharField(choices=FLOORS, max_length=len(FLOORS[0][0]), default=FLOORS[1][0])
    doer_resident = models.OneToOneField('Resident', models.SET_NULL, null=True, blank=True, related_name='lives_in')
    available = models.BooleanField(default=True)

    def __str__(self):
        floor = str(self.floor)[-3::-1][::-1]
        to_ret = self.name
        match floor:
            case 'Ground':
                to_ret = 'Ground'
            case '1':
                to_ret = '01-' + to_ret
            case '2':
                to_ret = '02-' + to_ret
            case '3':
                to_ret = '03-' + to_ret
            case '4':
                to_ret = '04-' + to_ret
            case '5':
                to_ret = '05-' + to_ret
            case '6':
                to_ret = '06-' + to_ret
            case '7':
                to_ret = '07-' + to_ret
            case '8':
                to_ret = '08-' + to_ret
            case '9':
                to_ret = '09-' + to_ret
            case '10':
                to_ret = '10-' + to_ret

        return to_ret


class Resident(models.Model):
    # Record: his_her_entries
    human = models.OneToOneField(Human, models.SET_NULL, null=True, blank=True, related_name='the_resident')
    accommodation = models.ForeignKey(Block, models.SET_NULL, null=True, blank=True, related_name='residents_here')
    resident_id = models.CharField(max_length=10, default='RS-', unique=True, validators=[resident_id_validator])

    def __str__(self):
        return self.resident_id


# validators=[lambda human_id: guard_gender_validator(Human.objects.get(pk=human_id).gender)]

class Guard(models.Model):
    # Record: taken_records
    human = models.OneToOneField(Human, models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='the_guard')
    salary = models.PositiveIntegerField('Guards monthly payment', default=0)
    guard_id = models.CharField(max_length=10, default='GA-', unique=True, validators=[guard_id_validator])

    def __str__(self):
        return self.guard_id


class TempToken(models.Model):
    key = models.CharField(max_length=12, default=get_a_token(), validators=[token_validator], unique=True)
    nag = models.PositiveSmallIntegerField('Number of allowed guests', default=1)
    nou = models.PositiveSmallIntegerField('Number of guests used this token', default=0)
    fond_by = models.ForeignKey(Resident, models.CASCADE, related_name='gained_tokens')
    used = models.BooleanField(default=False)
    valid_till = models.DateTimeField()

    def __str__(self):
        return self.key + ': ' + str(self.fond_by)

    def new_token(self):
        return get_a_token()

    def can_inc_nou(self):
        if self.nou < self.nag:
            return True
        return False

    def inc_nou(self):
        if self.can_inc_nou():
            self.nou += 1
        else:
            raise PermissionError('Number of max allowed guests reached.')


class Guest(models.Model):
    # token = (32 - len(token)) * '0' + token
    # token = token[:32]
    # if token is validated, return his resident with details
    # guest_id is: GS-last 7 digit of token
    guest_id = models.CharField(max_length=10, default='GS-', unique=True, validators=[guest_id_validator])
    token = models.ForeignKey(TempToken, models.SET_NULL, null=True, blank=True, related_name='guests')
    guest_of = models.ForeignKey(Resident, models.CASCADE, related_name='guests')
    photo = models.ImageField(upload_to='guests')
    nid_or_br = models.CharField(verbose_name='National Identity/Birth Registration No.', max_length=32)


class Record(models.Model):
    ENTRY = 'entry'
    EXIT = 'exit'
    TYPE = [
        (ENTRY, 'Entry'),
        (EXIT, 'Exit'),
    ]
    largest_type_len = max(len(t[0]) for t in TYPE)

    who = models.ForeignKey(Resident, models.SET_NULL, null=True, related_name='his_her_entries')
    # who = models.CharField(max_length=10, validators=[who_id_validator], default='RS-demo')
    e_type = models.CharField(choices=TYPE, max_length=largest_type_len, default=ENTRY)
    timestamp = models.DateTimeField(auto_now_add=True)
    recorder = models.ForeignKey(Guard, models.SET_NULL, null=True, blank=True, related_name='taken_records')

    def __str__(self):
        return str(self.who) + ': ' + str(self.e_type)


class Issue(models.Model):
    title = models.CharField(verbose_name='Problem title', max_length=100)
    details = models.TextField(verbose_name='Problem detail')
    raised_by = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='issues')
    raised_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    emergency = models.BooleanField(default=False)
    checked = models.BooleanField('Checked by admin', default=False)  # set true when admin views it
    resolved = models.BooleanField('Admin taken necessary steps to resolve this issue', default=False)

    def __str__(self):
        return self.title + ' - ' + self.raised_by.human.user.get_username()

    def edited(self):
        return self.raised_at != self.last_updated


class Bill(models.Model):
    ROOM_RENT = 'RENT'
    WATER = 'WATER'
    ELECTRICITY = 'ELECTRICITY'
    WASTE_DISPOSAL = 'WASTE DISPOSAL'
    SECURITY = 'SECURITY'
    PARKING = 'PARKING'
    OTHER = 'OTHER'
    BILL_TYPES = [
        (ROOM_RENT, 'ROOM RENT'),
        (WATER, 'WATER'),
        (ELECTRICITY, 'ELECTRICITY'),
        (WASTE_DISPOSAL, 'WASTE DISPOSAL'),
        (SECURITY, 'SECURITY'),
        (PARKING, 'PARKING'),
        (OTHER, 'OTHER'),
    ]
    lar_bill_type_len = max(len(bt[1]) for bt in BILL_TYPES)

    description = models.TextField(verbose_name="Bill's description", null=True, blank=True)
    tnx_nmr = models.CharField(verbose_name='Transaction number', max_length=100, null=True, blank=True, unique=True)
    bill_type = models.CharField(verbose_name='Bill for which',
                                 max_length=lar_bill_type_len,
                                 choices=BILL_TYPES,
                                 default=ROOM_RENT)
    amount = models.PositiveIntegerField(verbose_name='Payable amount')
    billed_to = models.ForeignKey(Resident, models.CASCADE, related_name='bills')  # SET IT BY HIS/HER USER-NAME
    granted = models.BooleanField(verbose_name='Granted-? (admin only)',
                                  default=False)  # only admin can edit, shows as paid(granted)/unpaid(un-resolved)/pending(admin view not happen) at Resident View.
