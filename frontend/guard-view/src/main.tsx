import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
import "preline";

import { HashRouter } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "react-query";
import {
  ReactQueryDevtools,
} from "react-query/devtools";

const client = new QueryClient();

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <HashRouter>
      <QueryClientProvider client={client}>
        <App />
        <ReactQueryDevtools />
      </QueryClientProvider>
    </HashRouter>
  </React.StrictMode>
);
