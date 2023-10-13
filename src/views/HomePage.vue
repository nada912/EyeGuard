<template>
    <div>
        <h1 class="text-center my-5">EyeGuard: Early Cancer Detection for Brighter Tomorrows</h1>
        <CarouselComponent />
    </div>
</template>

<script>
import CarouselComponent from "../components/CarouselComp.vue";
export default {
    name: "HomePage",
    components: {
        CarouselComponent
    },
   
};
</script>

<style>
h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

p {
    font-size: 1.5rem;
}
</style>
