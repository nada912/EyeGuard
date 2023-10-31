<template>
    <div class="slide" v-bind:style="{ width: slideWidth }" @click="$emit('slideClick')">
      <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'SlideComponent',
    props: {
      slideWidth: {
        type: String,
        default: '100%'
      }
    }
}
</script>

<style scoped>
.slide {
    scroll-snap-align: start;
    flex-shrink: 0;
    width: 100%;
    height: auto;
    border-radius: 1em;
    background-color: #fff;
    transform-origin: center center;
    transform: scale(1);
    transition: transform 0.5s;
    position: relative;
    padding: 1rem;
}
</style>
