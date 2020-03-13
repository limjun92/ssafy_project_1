import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8000/api/v1",
  // baseURL: "http://i02c102.p.ssafy.io:8000/api/v1",
  //baseURL: "https://i02c102.p.ssafy.io:8000/api/v1",
  headers: {
    "Content-type": "application/json",
  }
});
