/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import "./style.css";

export const Card = ({
  className,
  frameClassName,
  divClassName,
  text = "آجیل خوری میناکاری اصفهان",
  divClassNameOverride,
  text1 = "۷۷۷٬۰۰۰ تومان",
}) => {
  return (
    <div className={`card ${className}`}>
      <div className={`frame-2 ${frameClassName}`} />
      <div className={`text-wrapper-2 ${divClassName}`}>{text}</div>
      <div className={`text-wrapper-3 ${divClassNameOverride}`}>{text1}</div>
      <button className="button">
        <div className="text-wrapper-4">افزودن به سبد خرید</div>
      </button>
    </div>
  );
};

Card.propTypes = {
  text: PropTypes.string,
  text1: PropTypes.string,
};
