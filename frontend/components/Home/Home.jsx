import PropTypes from "prop-types";
import React from "react";
import { useReducer } from "react";
import { Link } from "react-router-dom";

export const Home = ({ property1, className, text = "خانه", divClassName, to }) => {
  const [state, dispatch] = useReducer(reducer, {
    property1: property1 || "default",
  });

  return (
    <Link
      className={`home property-1-11-${state.property1} ${className}`}
      to={to}
      onMouseLeave={() => {
        dispatch("mouse_leave");
      }}
      onMouseEnter={() => {
        dispatch("mouse_enter");
      }}
    >
      <div className={`text-wrapper-15 ${divClassName}`}>{text}</div>
    </Link>
  );
};

function reducer(state, action) {
  switch (action) {
    case "mouse_enter":
      return {
        ...state,
        property1: "variant-2",
      };

    case "mouse_leave":
      return {
        ...state,
        property1: "default",
      };
  }

  return state;
}

Home.propTypes = {
  property1: PropTypes.oneOf(["variant-2", "default"]),
  text: PropTypes.string,
  to: PropTypes.string,
};
