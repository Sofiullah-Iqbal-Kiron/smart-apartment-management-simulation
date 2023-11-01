import { Hero } from "../components/profilepage/Hero";
import { Bills } from "../components/profilepage/Bills";
import { Activities } from "../components/profilepage/Activities";
import { AfterHero } from "../components/profilepage/AfterHero";
import TopBlank from "../components/TopBlank";
import { useState, useEffect } from "react";
import axios from "axios";
import { useBasicAuth, useResidentProfileData } from "../store";
import { endpoints } from "../api/endpoints";
import Issues from "../components/profilepage/Issues";

function BlankSpace() {
  return <div className="h-[3rem]" />;
}

export function ProfilePage() {
  const {username, password} = useBasicAuth()
  const {residentProfileData, setResidentProfileData} = useResidentProfileData()

  const fetchProfileData = () => {
    axios
      .get(endpoints.my_profile, {
        auth: { username: username, password: password },
      })
      .then((res) => setResidentProfileData(res.data))
      .catch((err) => console.log(err));
  };

  useEffect(()=>fetchProfileData(), [])

  return (
    <section className="px-1.5">
      <TopBlank />

      <h1 className="text-center text-4xl my-3">Resident Profile</h1>

      <Hero
        username={residentProfileData.human.user.username}
        fullname={residentProfileData.human.user.fullname}
        accommodation={`${residentProfileData.accommodation.floor} floor, Flat-${residentProfileData.accommodation.label}`}
        since={residentProfileData.human.user.since}
        avatar_link={residentProfileData.human.avatar}
        rs_id={residentProfileData.ID}
      />

      <BlankSpace />

      <AfterHero/>

      <BlankSpace />

      {/* <Bills />

      <BlankSpace /> */}

      <Activities />

      <BlankSpace />

      <Issues />

      <BlankSpace />
    </section>
  );
}
