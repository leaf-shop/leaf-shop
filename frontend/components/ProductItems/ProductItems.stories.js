import { ProductItems } from ".";

export default {
  title: "Components/ProductItems",
  component: ProductItems,
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
    text: "فیروزه کوبی",
    line: "https://c.animaapp.com/VKfJiElF/img/line-6-5.svg",
  },
};
