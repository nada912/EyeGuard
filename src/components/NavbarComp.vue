<template>
  <nav class="navbar">
    <div class="container mx-auto flex justify-between items-center">
      <div class="logo">
        <img src="../assets/nv_logo.png" alt="Logo" class="w-12 h-12" />
      </div>
      <div class="EyeGuardT">EyeGuard</div>
      <ul class="nav-links flex space-x-4">
        <li><router-link to="/" class="text-white">Home</router-link></li>
        <li><router-link to="/check-cancer" class="text-white">Check Cancer</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavbarComponent',
  data() {
    return {
      Title: 'EyeGuard',
    };
  },
};
</script>

<style scoped>
.navbar {
  position: sticky;
  z-index: 100;
  width: 100%;
  background-color:none;
  padding: 10px;
  margin: 0% 0% 0% 0%;
  display: flex;
  align-items: flex-start; 
  justify-content: space-between;
  transition: all 0.3s ease-in-out;
  cursor: pointer;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
}

.nav-content {
  display: flex;
  justify-content: space-between;
  align-items: center; /* Center the content vertically */
}

.logo {
  width: 5%;
  margin-left: 1%;
  margin-bottom: 0%;
}

.EyeGuardT {
  font-size: 40px;
  font-weight: bold;
  margin-right: 53%;
  color: rgb(49, 141, 98);
}

.nav-links {
  display: flex;
  list-style-type: none;
  margin-left: 11%;
}

.nav-links li {
  margin: 0 10px;
}

.nav-links a {
  text-decoration: none;
  color: #333;
}

.nav-links a:hover {
  color: rgb(49, 141, 98);
}
</style>
