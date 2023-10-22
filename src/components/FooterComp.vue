<template>
    <footer class="footer">
        <div class="container">
            <ul class="footer-links">
                <li><router-link to="/about-us">About Us</router-link></li>
                <li><router-link to="/confidentiality">Privacy Policy</router-link></li>

            </ul>
        </div>
    </footer>

</template>

<script>
export default {
    name: 'FooterComponent'
}
</script>

<style scoped>
.footer {
  background-color: rgb(49, 141, 98);
  color: white;
  text-align: center;
  padding: 20px 0;
  margin-bottom: 0;
  width: 100%;
  grid-template-rows: 1fr auto;
}

.footer-links {
  display: flex;
  justify-content: center;
  align-items: center;
  list-style-type: none;
  padding: 0;
  color: white;
}

.footer-links li {
  margin: 0 10px;
}

.footer-links li a {
  color: white;
  text-decoration: none;
}

.footer-links li a:hover {
  color:black;
}
</style>

