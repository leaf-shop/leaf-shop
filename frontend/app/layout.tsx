import type { Metadata } from "next";
import { Inter } from "next/font/google";
import localFont from "next/font/local";
import "./globals.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const inter = Inter({ subsets: ["latin"] });
const samim = localFont({
  src: [
    {
      path: './fonts/samim/Samim-FD.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './fonts/samim/Samim-Bold-FD.woff2',
      weight: '700',
      style: 'normal',
    },
  ],
})

export const metadata: Metadata = {
  title: "Leaf Shop",
  description: "Make it easy!",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body dir="rtl" className={inter.className +" "+ samim.className}>
        <Navbar />
        <div className="h-[100vh] mt-[68px] p-5">{children}</div>
        <Footer />
      </body>
    </html>
  );
}
