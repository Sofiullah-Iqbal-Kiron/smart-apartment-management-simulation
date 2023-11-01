import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { endpoints } from "./endpoints";

const fetchIssuesConfig = {}
const fetchIssues = () => axios.get(endpoints.issues, fetchIssuesConfig).then((res) => res.data).catch((err) => console.log(err))
export const useIssues = () => useQuery({ queryKey: ["issues"], queryFn: fetchIssues })

const fetchResidentsConfig = {}
const fetchResidents = () => axios.get(endpoints.residents, fetchResidentsConfig).then((res) => res.data).catch(err => console.log(err))
export const useResidents = () => useQuery({ queryKey: ["residents"], queryFn: fetchResidents })

const fetchGuardsConfig = {}
const fetchGuards = () => axios.get(endpoints.guards, fetchGuardsConfig).then(res => res.data).catch(err => console.log(err))
export const useGuards = () => useQuery({ queryKey: ["guards"], queryFn: fetchGuards })