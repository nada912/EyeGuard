<template>
    <nav class="navbar">
        <div class="container">
            <div class="nav-content">
                <img class="logo" src="../assets/logo.png" alt="Logo" />
                <span class="EyeGuardT">{{ Title }}</span>
                <ul class="nav-links">
                    <li><router-link to="/">Home</router-link></li>
                    <li><router-link to="/check-cancer">Check Cancer</router-link></li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavbarComponent',
    data() {
    return {
      Title : 'EyeGuard'
    };
  },
}
</script>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  width: 100%;
  background-color: white;
  padding: 10px;
  align-items: center;
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
}

.logo {
  width: 5%;
  align-self: left;
  margin-left: 1%;
  margin-bottom: 0%;
}

.EyeGuardT {
    font-size: 40px;
    font-weight: bold;
    margin-left: 16%;
}

.nav-links {
  display: flex;
  list-style-type: none;
  margin-right: 8%;
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
