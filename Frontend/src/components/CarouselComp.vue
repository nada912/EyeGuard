<template>
  <div class="carousel  flex items-center justify-center">
    <div v-for="(slide, index) in slides" :key="index">
      <Slide v-if="currentSlide === index" @slideClick="nextSlide">
        <img :src="slide.image" />
        <h3>{{ slide.title }}</h3>
        <p>{{ slide.description }}</p>
      </Slide>
    </div>
  </div>
</template>


<script>
import Slide from './Slide';

export default {
  components: { Slide },
  name: 'CarouselComponent',
  props: {
    slides: Array,
    interval: {
      type: Number,
      default: 3500
    }
  },
  data() {
    return {
      currentSlide: 0
    };
  },
  mounted() {
    setInterval(() => {
      this.nextSlide();
    }, this.interval);
  },
  methods: {
    nextSlide() {
      if (this.currentSlide < this.slides.length - 1) {
        this.currentSlide++;
      } else {
        this.currentSlide = 0;
      }
    },
  },
};
</script>

<style scoped>
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

.carousel img {
  max-height: 500px;
  width: 100%;
  height: auto;
  object-fit: cover;
}

</style>
