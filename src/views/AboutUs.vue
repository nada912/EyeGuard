<template>
    <div class="about-us">
        <h1>About Us</h1>
        <p>We are a team of passionate developers who love creating innovative solutions to real-world problems. Our mission is to make the world a better place through technology.
        The EyeGuard project is a Cancer Detection project aims to develop a web-based application that allows users to
        upload images of eyes for cancer detection. The system utilizes machine learning models to
        analyze uploaded images and provide a likelihood score indicating the presence of cancer. 
        </p>
        <h2>Our Team</h2>
        <ul>
            <li v-for="(member, index) in team" :key="index">{{ member.name }} - {{ member.role }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            team: [
                { name: 'Nada NADIRE', role: 'Frontend Developer', image: require('@/assets/girl.png')},
                { name: 'Hamza HORD', role: 'Backend Developer', image: require('@/assets/boy.png') },
                { name: 'Yann Zeutsop', role: 'UI/UX Designer', image: require('@/assets/boy.png') },
            ]
        }
    }
}
</script>

<style>
.about-us {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}
.about-us h1 {
    font-size: 36px;
    margin-bottom: 20px;
}
.about-us h2 {
    font-size: 24px;
    margin-top: 40px;
    margin-bottom: 20px;
}
.about-us ul {
    list-style: none;
    margin: 0;
    padding: 0;
}
.about-us li {
    margin-bottom: 10px;
}
</style>
