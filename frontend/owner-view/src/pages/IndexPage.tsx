import PageHeader from "../components/Headers/PageHeader";
import SectionHeader from "../components/Headers/SectionHeader";
import BlankSpace from "../components/BlankSpace";

export default function IndexPage() {
  return (
    <div className="flex flex-col justify-center items-center">
      <PageHeader text="Owner Home" />

      <section className="w-4/5">
        <SectionHeader text="Actions" />
        <div className="w-full join join-vertical">
          <a href="#manage-guards" className="w-full btn btn-primary btn-square join-item">Manage Guards</a>
          <button className="w-full btn btn-secondary btn-square join-item">Manage Residents</button>
          <button className="w-full btn btn-success btn-square join-item">Manage Blocks</button>
          <button className="w-full btn btn-info btn-square join-item">Handle Issues</button>
        </div>
      </section>

      <section id="manage-guards" className="w-4/5">
        <SectionHeader text="Manage Guards" />
        <div className="w-full join join-vertical">
          <button className="w-full btn btn-primary btn-square join-item">Add a new guard</button>
          <button className="w-full btn btn-secondary btn-square join-item">Manage Residents</button>
          <button className="w-full btn btn-success btn-square join-item">Manage Blocks</button>
          <button className="w-full btn btn-info btn-square join-item">Handle Issues</button>
        </div>
      </section>
      
      <section className="w-4/5">
        <SectionHeader text="Manage Residents" />
        <div className="w-full join join-vertical">
          <button className="w-full btn btn-primary btn-square join-item">Add a new resident</button>
          <button className="w-full btn btn-secondary btn-square join-item">Manage Residents</button>
          <button className="w-full btn btn-success btn-square join-item">Manage Blocks</button>
          <button className="w-full btn btn-info btn-square join-item">Handle Issues</button>
        </div>
      </section>

      <BlankSpace />

    </div>
  );
}
