import React from 'react'
import Image from 'next/image'

function HeaderSection() {
  return (
    <section className='grid grid-cols-2 w-100 my-10'>
      <div className='flex flex-col items-center'>
        <article className="prose">
          <h1>بهترین صنایع دستی را از فروشگاه زینتکده بخر!</h1>
          <span>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.</span>
        </article>
      </div>
      <div className='flex justify-center'>
        <div className='relative'>
          <Image
            className='h-[60vh] w-auto'
            src="/images/image1.png"
            width={500}
            height={500}
            alt="Picture of the author"
          />
          <Image
            src="/images/image2.png"
            className='h-[20vh] w-auto absolute -right-16 -bottom-16'
            width={500}
            height={500}
            alt="Picture of the author"
          />
        </div>
      </div>
    </section>
  )
}

export default HeaderSection