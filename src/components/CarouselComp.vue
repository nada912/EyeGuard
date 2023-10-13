<template>
    <div class="carousel-container">
      <carousel>
        <slide v-for="(item, index) in items" :key="index">
          <div class="carousel-item">
            <img :src="item.image" alt="Carousel Image">
          </div>
        </slide>
      </carousel>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        items: [
          { image: "" },
          { image: "" },
          { image: "" },
        ],
      };
    },
  };
  </script>
  

<style>
    .carousel-container {
        max-width: 800px;
        margin: 0 auto;
    }

    .carousel-item img {
        max-width: 100%;
        height: auto;
    }
        
</style>

  