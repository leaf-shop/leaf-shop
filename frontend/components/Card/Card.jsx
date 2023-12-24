import PropTypes from "prop-types";
import React from "react";

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
