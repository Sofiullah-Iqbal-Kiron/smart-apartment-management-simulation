export function RecordGuestForm() {
	return (
		<section>
			<form className='flex flex-col justify-center items-center space-y-5'>
				<legend className='text-3xl mb-8'>
					Record Guest
				</legend>

				<div className="flex flex-col justify-center items-start space-y-1">
					<label>
						Guest ID
					</label>
					<input type='text'/>
				</div>

				<div className="flex flex-col justify-center items-start space-y-2">
					<label>
						label2
					</label>
					<input type="text"/>
				</div>
			</form>
		</section>
	)
}