'use client' 

import PropTypes from "prop-types";
import React from "react";
import { useReducer } from "react";
import { ProductItems } from "../ProductItems";

export const Products = ({ property1, className }) => {
  const [state, dispatch] = useReducer(reducer, {
    property1: property1 || "default",
  });

  return (
    <div className={`products ${className}`}>
      <div className={`group property-1-8-${state.property1}`}>
        <img
          className="image"
          alt="Image"
          src={
            state.property1 === "variant-2"
              ? "https://c.animaapp.com/VKfJiElF/img/khatam-art5-1.png"
              : state.property1 === "variant-3"
              ? "https://c.animaapp.com/VKfJiElF/img/gaz-khori-1-logo.png"
              : state.property1 === "variant-4"
              ? "https://c.animaapp.com/VKfJiElF/img/5-24.png"
              : "https://c.animaapp.com/VKfJiElF/img/image-5.png"
          }
        />
        <img
          className="image-2"
          alt="Image"
          src={
            state.property1 === "variant-2"
              ? "https://c.animaapp.com/VKfJiElF/img/2d3a9296-f9bf-4390-aeb5-e0e77863a40e-1.png"
              : state.property1 === "variant-3"
              ? "https://c.animaapp.com/VKfJiElF/img/1396012112033529510489864-1.png"
              : state.property1 === "variant-4"
              ? "https://c.animaapp.com/VKfJiElF/img/turquoise2-jewelry2-set13.png"
              : "https://c.animaapp.com/VKfJiElF/img/image-4.png"
          }
        />
      </div>
      <div className="frame-3">
        <ProductItems
          className="product-items-instance"
          line={state.property1 === "variant-4" ? "https://c.animaapp.com/VKfJiElF/img/line-6-2.svg" : undefined}
          onClick={() => {
            dispatch("click");
          }}
          property1={state.property1 === "variant-4" ? "variant-2" : "default"}
          text="جواهرات"
        />
        <ProductItems
          className="product-items-instance"
          line={state.property1 === "variant-3" ? "https://c.animaapp.com/VKfJiElF/img/line-6-3.svg" : undefined}
          onClick={() => {
            dispatch("click_289");
          }}
          property1={state.property1 === "variant-3" ? "variant-2" : "default"}
          text="میناکاری"
        />
        <ProductItems
          className="product-items-instance"
          line={state.property1 === "variant-2" ? "https://c.animaapp.com/VKfJiElF/img/line-6-4.svg" : undefined}
          onClick={() => {
            dispatch("click_292");
          }}
          property1={state.property1 === "variant-2" ? "variant-2" : "default"}
          text="خاتم کاری"
        />
        <ProductItems
          className="product-items-instance"
          onClick={() => {
            dispatch("click_329");
          }}
          property1={state.property1 === "default" ? "variant-2" : "default"}
          text="فیروزه کوبی"
        />
      </div>
    </div>
  );
};

function reducer(state, action) {
  if (state.property1 === "default") {
    switch (action) {
      case "click":
        return {
          property1: "variant-4",
        };

      case "click_289":
        return {
          property1: "variant-3",
        };
    }
  }

  if (state.property1 === "variant-3") {
    switch (action) {
      case "click":
        return {
          property1: "variant-4",
        };

      case "click_329":
        return {
          property1: "default",
        };
    }
  }

  if (state.property1 === "variant-4") {
    switch (action) {
      case "click_289":
        return {
          property1: "variant-3",
        };

      case "click_329":
        return {
          property1: "default",
        };
    }
  }

  switch (action) {
    case "click_292":
      return {
        ...state,
        property1: "variant-2",
      };
  }

  return state;
}

Products.propTypes = {
  property1: PropTypes.oneOf(["variant-4", "variant-2", "variant-3", "default"]),
};
