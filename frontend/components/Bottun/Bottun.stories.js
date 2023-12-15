import { Bottun } from ".";

export default {
  title: "Components/Bottun",
  component: Bottun,
  argTypes: {
    property1: {
      options: ["variant-2", "default"],
      control: { type: "select" },
    },
  },
};

export const Default = {
  args: {
    property1: "variant-2",
    className: {},
    iconsaxLinear: "https://c.animaapp.com/VKfJiElF/img/iconsax-linear-arrowdown-4.svg",
  },
};
