import PropTypes from "prop-types";
import React from "react";
import { useReducer } from "react";

export const Bottun = ({
  property1,
  className,
  iconsaxLinear = "https://c.animaapp.com/VKfJiElF/img/iconsax-linear-arrowdown-4.svg",
}) => {
  const [state, dispatch] = useReducer(reducer, {
    property1: property1 || "default",
  });

  return (
    <div
      className={`bottun ${className}`}
      onMouseEnter={() => {
        dispatch("mouse_enter");
      }}
    >
      <div className="text-wrapper">همین حالا خرید کن</div>
      <img className={`iconsax-linear ${state.property1}`} alt="Iconsax linear" src={iconsaxLinear} />
    </div>
  );
};

function reducer(state, action) {
  if (state.property1 === "default") {
    switch (action) {
      case "mouse_enter":
        return {
          property1: "variant-2",
        };
    }
  }

  if (state.property1 === "variant-2") {
    switch (action) {
      case "mouse_enter":
        return {
          property1: "default",
        };
    }
  }

  return state;
}

Bottun.propTypes = {
  property1: PropTypes.oneOf(["variant-2", "default"]),
  iconsaxLinear: PropTypes.string,
};
