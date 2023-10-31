<template>
    <section>
        <h1>About us:</h1>
        <p>We are a team of passionate developers who love creating innovative solutions to real-world problems. 
        Our mission is to make the world a better place through technology.
        The EyeGuard project is a Cancer Detection project aims to develop a web-based application that allows users to
        upload images of eyes for cancer detection. The system utilizes machine learning models to
        analyze uploaded images and provide a likelihood score indicating the presence of cancer. 
        </p>
        <h2>Our team:</h2>
        <div class="team">
          <div class="card" v-for="member in teamMembers" :key="member.id">
            <img :src="member.image" alt="Team member">
            <div class="card-body">
              <h3 class="card-title">{{ member.name }}</h3>
              <p class="card-text">{{ member.role }}</p>
            </div>
          </div>
        </div>
    </section>
</template>

<script>
export default {
    data() {
        return {
            teamMembers: [
                { id: 1, name: 'Nada NADIRE', role: 'Frontend & Azure Developer', image: require('@/assets/girl.png')},
                { id: 2, name: 'Hamza HORD', role: 'Backend Developer', image: require('@/assets/boy.png') },
                { id: 3, name: 'Yann Zeutsop', role: 'UI/UX Designer', image: require('@/assets/boy.png') },
            ],
        };
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

section {
    font-family: 'Roboto', sans-serif;
    margin: 0 auto;
    max-width: 900px;
    padding: 20px;
    color: #333;
    line-height: 1.7;
}

h1, h2 {
    color: rgb(49, 141, 98);
}

h1 {
    font-size: 2.2em;
    margin-bottom: 0.75em;
}

h2 {
    font-size: 1.8em;
    margin-top: 2em;
    margin-bottom: 1em;
}

p {
    font-size: 1.1em;
    margin-bottom: 1.2em;
}

ul {
    padding-left: 20px;
    margin-bottom: 1.2em;
}

ul li {
    margin-bottom: 0.6em;
}

.team {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 2em;
}

.card {
  background-color: #f8f8f8;
  border-radius: 10px;
  box-shadow: 0 4px 6px 0 hsla(0, 0%, 0%, 0.2);
  overflow: hidden;
  margin-bottom: 2em;
  width: calc(33.333% - 1em); /* Change the card width to one third */
}

.card img {
  width: 100%;
  object-fit: contain;
}

.card-body {
  padding: 1.5em;
}

.card-title {
  font-size: 1.4em;
  margin-bottom: 0.5em;
}

.card-text {
  color: #666;
}
</style>
