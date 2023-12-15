/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import "./style.css";

export const ProductItems = ({
  property1,
  className,
  text = "فیروزه کوبی",
  onClick,
  line = "https://c.animaapp.com/VKfJiElF/img/line-6-5.svg",
}) => {
  return (
    <div className={`product-items ${className}`} onClick={onClick}>
      <div className={`text-wrapper-6 property-1-7-${property1}`}>{text}</div>
      {property1 === "variant-2" && <img className="line" alt="Line" src={line} />}
    </div>
  );
};

ProductItems.propTypes = {
  property1: PropTypes.oneOf(["variant-2", "default"]),
  text: PropTypes.string,
  line: PropTypes.string,
};
