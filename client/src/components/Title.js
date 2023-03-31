import React, {useState, useEffect} from 'react';

import Me from './Me.png'
import wave1 from './wave1.svg'
import wave2 from './wave2.svg'
import wave3 from './wave3.svg'

const Title = () => {
  return (
    <div className="Title flex  flex-a-i flex-f-d-c">
        <img alt='wave1' src={wave1} className='wave wave-1'/>
        <img alt='wave2' src={wave2} className='wave wave-2'/>
        <img alt='wave3' src={wave3} className='wave wave-3'/>
        <section className='flex aboutMe'>
            <img alt='Me' src={Me} className='Title__img'/>
        </section>
    </div>
    );
  }
  
export default Title;