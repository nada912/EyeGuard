<template>
    <header>
        <div class="logo">
            <img src="path/to/logo.png" alt="Logo">
            <h1>{{ title }}</h1>
        </div>
    </header>
</template>

<script>
export default {
    name: 'Header',
    data() {
        return {
            title: 'EyeGuard'
        }
    }
}
</script>

<style>
header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
}

.logo {
    display: flex;
    align-items: center;
}

.logo img {
    height: 50px;
    margin-right: 1rem;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
}

nav li {
    margin-right: 1rem;
}

nav a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}
</style>
