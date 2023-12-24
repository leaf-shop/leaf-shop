import PropTypes from "prop-types";
import React from "react";

export const ProductItems = ({
  property1,
  className,
  text = "فیروزه کوبی",
  onClick,
}) => {
  return (
    <div className={`product-items ${className}`} onClick={onClick}>
      <div className={`hover:text-blue-700 hover:border-b-2 border-blue-700 cursor-pointer text-wrapper-6 property-1-7-${property1}`}>{text}</div>
    </div>
  );
};

ProductItems.propTypes = {
  property1: PropTypes.oneOf(["variant-2", "default"]),
  text: PropTypes.string,
  line: PropTypes.string,
};
