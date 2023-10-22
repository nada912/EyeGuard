<template>
  <div class="slogan-container">
    <div class="slogan w-full sm:w-1/2 text-center p-5 sm:p-10">
      <h1 class="text-3xl sm:text-4xl lg:text-5xl text-green-500">Early Cancer Detection</h1>
      <h2 class="text-2xl sm:text-3xl lg:text-4xl">for Brighter Tomorrows</h2>
    </div>
  </div>  
  <div class="container">
    <div class="content">
      <Carousel :slides="slides" @nextSlide="nextSlide()" @previousSlide="previousSlide()">
        <template v-for="(slide, index) in slides" :key="index">
          <Slide v-if="currentSlide === index">
            <img :src="slide.image" />
            <h3>{{ slide.title }}</h3>
            <p>{{ slide.description }}</p>
          </Slide>
        </template>
      </Carousel>
      <div class="info-card">
        <p>This website allows users to upload images of their eyes for cancer detection.
          The system utilizes machine learning models to analyze uploaded images and provide a likelihood score 
          indicating the presence of cancer.
        </p>
      </div>

    </div>

    <div class="card-container">
      <div
        class="event-card"
        v-for="(event, index) in events"
        :key="index"
        :class="{ 'responsive-class': shouldApplyResponsiveClass }"
      >
        <img :src="event.thumbnail" />
        <h3>{{ event.title }}</h3>
        <p>{{ event.date }}</p>
      </div>
    </div>

  </div>
  
  </template>
  
  <script>
  import Carousel from '@/components/CarouselComp.vue';
  import Slide from '@/components/Slide.vue';
  
  export default {
    components: {
      Carousel,
      Slide
    },
    
    data() {
      return {
        imageSrc: '',
        desiredWidth: 800,
        desiredHeight: 445,
  
        currentSlide: 0, // Index of the current slide
        slides: [
          {
            image: require('@/assets/girl.png'),
            title: 'Girl\'s picture',
            description: 'Picture of a girl',
          },
          {
            image: require('@/assets/boy.png'),
            title: 'Boy\'s picture',
            description: 'Picture of a boy',
        },
        ],
        events: [
          {
            id: 1,
            thumbnail: require('@/assets/girl.png'),
            title: 'Girl',
            date: '17 décembre 2022',
          },
          {
            id: 2,
            thumbnail: require('@/assets/logo.png'),
            title: 'Logo',
            date: '06 décembre 2022',
          },
          {
            id: 3,
            thumbnail: require('@/assets/boy.png'),
            title: 'Boy',
            date: '18 décembre 2022',
          },

        ],
      };
    },
    computed: {
      getImageStyle() {
        return {
          width: `${this.desiredWidth}px`,
          height: `${this.desiredHeight}px`
        };
      }
    },
    methods: {
      nextSlide() {
        this.currentSlide = (this.currentSlide + 1) % this.slides.length;
      },
      previousSlide() {
        this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
      }
    }
  
  };
  
</script>
  
<style scoped>
.slogan-container {
  display: flex;
  align-items: center;
  height: 100px; 
  margin: 0;
  padding: 0;
  position: relative;
  /*background-image: url('../assets/eye.png'); */
}

.slogan {
  width: 50%;
  text-align: center;
  padding: 10px;
  margin-left: 25%;
}

h1, h2 {
  font-size: 2rem; 
  color:  rgb(49, 141, 98);
  margin: 0;
}
.container {
  margin: 20px;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.info-card, .event-card {
  border-radius: 15px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  padding: 1rem;
  max-width: 500px;
  width: 100%;  /* ensures the card stretches to fill the space */
  height: auto; /* allows the card to adjust its height based on the content */
}

.info-card {
  margin: 20px;
  padding: 1rem;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 5px;

}

.event-card {
  border-radius: 15px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  padding: 1rem;
  width: 30%; /* defines a fixed width for the card */
  height: 100%; /* ensures the card stretches to fill the space */
}

.event-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.button-container {
  display: flex;
  justify-content: space-between;
}

.responsive-card {
    width: 100%;
    height: auto;
}

@media (max-width: 768px) {
  .responsive-card {
    width: 100%;
  }
}
</style>
