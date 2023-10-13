<template>
    <div>
        <h1 class="text-center my-5">EyeGuard: Early Cancer Detection for Brighter Tomorrows</h1>
        <b-carousel
            id="carousel-1"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333;"
        >
            <b-carousel-slide
                v-for="(slide, i) in slides"
                :key="i"
                :caption="slide.caption"
                :img-src="slide.img"
                :text="slide.text"
            ></b-carousel-slide>
        </b-carousel>
    </div>
</template>

<script>
export default {
    name: "HomePage",
    data() {
        return {
            slides: [
                {
                    img: "https://via.placeholder.com/1024x480.png?text=Slide+1",
                    caption: "Slide 1",
                    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                },
                {
                    img: "https://via.placeholder.com/1024x480.png?text=Slide+2",
                    caption: "Slide 2",
                    text: "Praesent commodo cursus magna, vel scelerisque nisl consectetur."
                },
                {
                    img: "https://via.placeholder.com/1024x480.png?text=Slide+3",
                    caption: "Slide 3",
                    text: "Nulla vitae elit libero, a pharetra augue mollis interdum."
                }
            ]
        };
    }
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
