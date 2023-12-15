import { AllComments } from ".";

export default {
  title: "Components/AllComments",
  component: AllComments,
  argTypes: {
    property1: {
      options: ["variant-2", "variant-3", "default"],
      control: { type: "select" },
    },
  },
};

export const Default = {
  args: {
    property1: "variant-2",
    className: {},
    ellipse: "https://c.animaapp.com/VKfJiElF/img/ellipse-3-11@2x.png",
    ellipseClassName: {},
    img: "https://c.animaapp.com/VKfJiElF/img/ellipse-3-10@2x.png",
    divClassName: {},
    ellipseClassNameOverride: {},
    ellipse1: "https://c.animaapp.com/VKfJiElF/img/ellipse-3-10@2x.png",
  },
};
