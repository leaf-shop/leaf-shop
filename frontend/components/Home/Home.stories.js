import { Home } from ".";

export default {
  title: "Components/Home",
  component: Home,
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
    text: "خانه",
    divClassName: {},
  },
};
