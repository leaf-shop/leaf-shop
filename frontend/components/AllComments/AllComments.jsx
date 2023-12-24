import PropTypes from "prop-types";
import React from "react";
import "./style.css";

export const AllComments = ({
  property1,
  className,
  ellipse = "https://c.animaapp.com/VKfJiElF/img/ellipse-3-11@2x.png",
  ellipseClassName,
  img = "https://c.animaapp.com/VKfJiElF/img/ellipse-3-10@2x.png",
  divClassName,
  ellipseClassNameOverride,
  ellipse1 = "https://c.animaapp.com/VKfJiElF/img/ellipse-3-10@2x.png",
}) => {
  return (
    <div className={`all-comments property-1-${property1} ${className}`}>
      <div className="comments">
        <div className="frame">
          <img
            className="ellipse"
            alt="Ellipse"
            src={property1 === "default" ? ellipse : "https://c.animaapp.com/VKfJiElF/img/ellipse-3-10@2x.png"}
          />
          <p className="div">
            لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون
            بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.
          </p>
          <div className="div-2">
            {["default", "variant-2"].includes(property1) && <>عاطفه صادقی</>}

            {property1 === "variant-3" && <>سعید کریمی</>}
          </div>
        </div>
      </div>
      <div className="frame-wrapper">
        <div className="frame">
          <img
            className={`img ${property1 === "default" ? ellipseClassName : undefined}`}
            alt="Ellipse"
            src={
              property1 === "variant-2"
                ? "https://c.animaapp.com/VKfJiElF/img/ellipse-3-7@2x.png"
                : property1 === "variant-3"
                ? "https://c.animaapp.com/VKfJiElF/img/ellipse-3-10@2x.png"
                : img
            }
          />
          <p className="div">
            لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون
            بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.
          </p>
          <div className={`div-3 ${property1 === "default" ? divClassName : undefined}`}>
            {property1 === "default" && <>سارا مالکی</>}

            {property1 === "variant-2" && <>سعید کریمی</>}

            {property1 === "variant-3" && <>عاطفه صادقی</>}
          </div>
        </div>
      </div>
      <div className="div-wrapper">
        <div className="frame">
          <img
            className={`ellipse-2 ${property1 === "default" ? ellipseClassNameOverride : undefined}`}
            alt="Ellipse"
            src={
              property1 === "variant-2"
                ? "https://c.animaapp.com/VKfJiElF/img/ellipse-3-10@2x.png"
                : property1 === "variant-3"
                ? "https://c.animaapp.com/VKfJiElF/img/ellipse-3-3@2x.png"
                : ellipse1
            }
          />
          <p className="div">
            لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون
            بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.
          </p>
          <div className="div-4">
            {property1 === "default" && <>سعید کریمی</>}

            {["variant-2", "variant-3"].includes(property1) && <>سارا مالکی</>}
          </div>
        </div>
      </div>
    </div>
  );
};

AllComments.propTypes = {
  property1: PropTypes.oneOf(["variant-2", "variant-3", "default"]),
  ellipse: PropTypes.string,
  img: PropTypes.string,
  ellipse1: PropTypes.string,
};
