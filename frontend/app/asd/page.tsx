"use client";

import React from "react";
import { AllComments } from "@/components/AllComments";
// import { Bottun } from "../../components/Bottun";
import { Card } from "@/components/Card";
// import { Footer } from "@/components/Footer";
// import { Navbar } from "@/components/Navbar";
import { Products } from "@/components/Products";
import { ReadMore } from "@/components/ReadMore";
import "./style.css";

export default function HomePage() {
  return (
    <div className="home-page">
      <div className="div-5">
        <div className="overlap">
          <div className="overlap-2">
            <p className="title">
              <span className="span">بهترین صنایع دستی را از فروشگاه </span>
              <span className="text-wrapper-19">زینتکده </span>
              <span className="span">بخر!</span>
            </p>
            <div className="overlap-3">
              <img className="image-3" alt="Image" src="https://c.animaapp.com/VKfJiElF/img/image1.png" />
              <img className="image-4" alt="Image" src="https://c.animaapp.com/VKfJiElF/img/image2@2x.png" />
            </div>
          </div>
          <p className="subtitle">
            لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون
            بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.
          </p>
          <div className="overlap-4">
            {/* <Bottun
              className="bottun-instance"
              iconsaxLinear="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-arrowdown.svg"
              property1="default"
            /> */}
            <img
              className="background-img"
              alt="Background img"
              src="https://c.animaapp.com/VKfJiElF/img/background-img-1@2x.png"
            />
            <img
              className="background-img-2"
              alt="Background img"
              src="https://c.animaapp.com/VKfJiElF/img/background-img@2x.png"
            />
          </div>
        </div>
        <div className="features">
          <div className="frame-9">
            <div className="group-7">
              <img
                className="iconsax-linear-star"
                alt="Iconsax linear"
                src="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-star1.svg"
              />
              <div className="text-wrapper-20">بهترین قیمت</div>
            </div>
            <div className="group-8">
              <img
                className="iconsax-linear-flag"
                alt="Iconsax linear"
                src="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-flag2.svg"
              />
              <div className="text-wrapper-20">بالاترین کیفیت</div>
            </div>
            <div className="group-9">
              <img
                className="iconsax-linear-cards"
                alt="Iconsax linear cards"
                src="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-cards.svg"
              />
              <div className="text-wrapper-20">پرداخت امن</div>
            </div>
            <div className="group-10">
              <img
                className="iconsax-linear-call"
                alt="Iconsax linear call"
                src="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-call.svg"
              />
              <div className="text-wrapper-20">پشتیبانی سریع</div>
            </div>
            <div className="group-11">
              <img
                className="iconsax-linear-truck"
                alt="Iconsax linear truck"
                src="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-truck.svg"
              />
              <div className="text-wrapper-21">تحویل اکسپرس</div>
            </div>
          </div>
        </div>
        <img
          className="background-img-3"
          alt="Background img"
          src="https://c.animaapp.com/VKfJiElF/img/background-img-3.png"
        />
        <AllComments
          className="all-comments-instance"
          divClassName="all-comments-2"
          ellipse="https://c.animaapp.com/VKfJiElF/img/ellipse-3-2@2x.png"
          ellipse1="https://c.animaapp.com/VKfJiElF/img/ellipse-3-1@2x.png"
          ellipseClassName="design-component-instance-node"
          ellipseClassNameOverride="all-comments-3"
          img="https://c.animaapp.com/VKfJiElF/img/ellipse-3-1@2x.png"
          property1="default"
        />
        <div className="title-2">نظر مشتریان زینتکده</div>
        <div className="product-cards">
          <Card
            className="card-instance"
            divClassName="frame-11"
            divClassNameOverride="frame-12"
            frameClassName="frame-10"
            text="گردنبند با سنگ فیروزه"
            text1="۸۰۰٬۰۰۰ تومان"
          />
          <Card
            className="card-instance"
            divClassName="frame-14"
            divClassNameOverride="frame-12"
            frameClassName="frame-13"
            text="کوزه لعابدار"
            text1="۹۲۰٬۰۰۰ تومان"
          />
          <Card
            className="card-instance"
            divClassName="frame-16"
            divClassNameOverride="frame-17"
            frameClassName="frame-15"
            text="آجیل خوری فیروزه کوبی اصفهان"
            text1="۲٬۲۰۰٬۰۰۰ تومان"
          />
          <Card
            className="card-instance"
            divClassName="frame-19"
            divClassNameOverride="frame-20"
            frameClassName="frame-18"
            text="انگشتر فیروزه نیشابور"
            text1="۸۵۰٬۰۰۰ تومان"
          />
          <div className="frame-21">
            <div className="frame-22">
              <img
                className="rectangle"
                alt="Rectangle"
                src="https://c.animaapp.com/VKfJiElF/img/rectangle-1-1@2x.png"
              />
            </div>
            <div className="text-wrapper-22">ساعت دیواری میناکاری</div>
            <div className="text-wrapper-23">۲٬۷۵۰٬۰۰۰ تومان</div>
            <button className="button-3">
              <div className="text-wrapper-24">افزودن به سبد خرید</div>
            </button>
          </div>
          <Card
            className="card-instance"
            divClassNameOverride="card-3"
            frameClassName="card-2"
            text="آجیل خوری میناکاری اصفهان"
            text1="۱٬۶۰۰٬۰۰۰ تومان"
          />
        </div>
        <div className="see-more">
          <img
            className="iconsax-linear-2"
            alt="Iconsax linear"
            src="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-arrowdown-2.svg"
          />
          <div className="text-wrapper-25">مشاهده همه</div>
        </div>
        <div className="title-3">جدیدترین ها</div>
        <div className="about-us">
          <p className="text">
            لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون
            بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است. لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت
            چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.
          </p>
          <ReadMore className="read-more-instance" />
          <div className="title-4">درباره زینتکده</div>
          <img className="image-5" alt="Image" src="https://c.animaapp.com/VKfJiElF/img/image-2.png" />
          <img
            className="background-img-4"
            alt="Background img"
            src="https://c.animaapp.com/VKfJiElF/img/background-img-2.png"
          />
        </div>
        <div className="icon">
          <img
            className="iconsax-linear-3"
            alt="Iconsax linear"
            src="https://c.animaapp.com/VKfJiElF/img/iconsax-linear-arrowdown-1.svg"
          />
        </div>
        <Products className="products-instance" property1="default" />
        {/* <Footer
          className="footer-instance"
          divClassName="footer-3"
          divClassNameOverride="footer-5"
          groupClassName="footer-4"
          overlapGroupClassName="footer-2"
          whatsappSvg="https://c.animaapp.com/VKfJiElF/img/whatsapp-svg.svg"
        />
        <Navbar className="navbar-instance" homeDivClassName="navbar-2" property1="default" /> */}
      </div>
    </div>
  );
}
