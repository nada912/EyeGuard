<template>
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2023 EyeGuard. All Rights Reserved.</p>
                </div>
                <div class="col-md-6">
                    <ul class="list-inline text-md-right">
                        <li class="list-inline-item">
                            <router-link to="/about-us">About Us</router-link>
                        </li>
                        <li class="list-inline-item">
                            <router-link to="/confidentiality">Privacy Policy</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style>
footer {
    background-color: #f8f9fa;
    padding: 20px 0;
    margin-top: 50px;
}
</style>
