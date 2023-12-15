/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import { useReducer } from "react";
import "./style.css";

export const Iconsax = ({ property1 }) => {
  const [state, dispatch] = useReducer(reducer, {
    property1: property1 || "default",
  });

  return (
    <div
      className={`iconsax property-1-13-${state.property1}`}
      onMouseLeave={() => {
        dispatch("mouse_leave");
      }}
      onMouseEnter={() => {
        dispatch("mouse_enter");
      }}
    >
      {["default", "variant-3"].includes(state.property1) && (
        <img
          className="vector"
          alt="Vector"
          src={
            state.property1 === "variant-3"
              ? "https://c.animaapp.com/VKfJiElF/img/vector-3.svg"
              : "https://c.animaapp.com/VKfJiElF/img/vector-6.svg"
          }
        />
      )}

      {["variant-2", "variant-4"].includes(state.property1) && (
        <div className="overlap-group-2">
          <img
            className="vector-2"
            alt="Vector"
            src={
              state.property1 === "variant-2"
                ? "https://c.animaapp.com/VKfJiElF/img/vector-6.svg"
                : "https://c.animaapp.com/VKfJiElF/img/vector-3.svg"
            }
          />
          <div className="container">
            <div className="text-wrapper-16">۱</div>
          </div>
        </div>
      )}
    </div>
  );
};

function reducer(state, action) {
  if (state.property1 === "default") {
    switch (action) {
      case "mouse_enter":
        return {
          property1: "variant-3",
        };
    }
  }

  if (state.property1 === "variant-3") {
    switch (action) {
      case "mouse_leave":
        return {
          property1: "default",
        };
    }
  }

  if (state.property1 === "variant-2") {
    switch (action) {
      case "mouse_enter":
        return {
          property1: "variant-4",
        };
    }
  }

  if (state.property1 === "variant-4") {
    switch (action) {
      case "mouse_leave":
        return {
          property1: "variant-2",
        };
    }
  }

  return state;
}

Iconsax.propTypes = {
  property1: PropTypes.oneOf(["variant-4", "variant-2", "variant-3", "default"]),
};
