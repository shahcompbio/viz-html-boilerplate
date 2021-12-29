import "./App.css";

const App = ({ text }) => {
  return text;
};

// Put specific arguments here for development
const Dev = () => {
  return <App text={"Gonna run in Dev mode"} />;
};

const Prod = () => {
  return <App {...window.appArgs} />;
};

export default process.env.NODE_ENV === "development" ? Dev : Prod;
