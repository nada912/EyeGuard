<template>
    <header>
        <h1>{{ title }}</h1>
        <img :src="logoSrc" alt="Logo">
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

<style scoped>
header {
    display: flex;
    align-items: center;
}

h1 {
    margin-right: 10px;
}
</style>
