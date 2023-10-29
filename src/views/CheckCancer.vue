<template>
    <div>
        <h1 class="check-title">Check for Eye Cancer</h1>
        <input type="file" @change="onFileChange" class="file-input">
        <button @click="analyzeImage" class="analyze-button">Analyze Image</button>
        <div v-if="result" class="result-container">
            <h2 class="result-title">Result:</h2>
            <p class="result-text">{{ result }}</p>
        </div>
    </div>
</template>

<script>
//import axios from "axios";

export default {
    data() {
        return {
            image: null,
            result: null
        }
    },
    methods: {
        onFileChange(event) {
            this.image = event.target.files[0]
        },
        async analyzeImage() {
            const formData = new FormData();
            formData.append('image', this.image);
            /*try {
                const response = await axios.post("http://localhost:5000/getresults/", formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                this.result = response.data;
                console.log(this.result);
            } catch (error) {
                console.log(error);
            }*/
        
            try {
                const response = await fetch('/api/analyze-image', {
                    method: 'POST',
                    body: formData
                })
                const data = await response.json()
                this.result = data.result
            } catch (error) {
                console.error(error)
            }
        }
    }
}
</script>

<style scoped>
.check-title {
    font-size: 24px;
    margin-bottom: 20px;
    color: #333;
}

.file-input {
    margin-bottom: 10px;
}

.analyze-button {
    background-color:rgb(49, 141, 98);
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    border-radius: 20px;
}

.analyze-button:hover {
    background-color: rgb(19, 105, 65);
}

.result-container {
    margin-top: 20px;
}

.result-title {
    font-size: 20px;
    margin-bottom: 10px;
    color: #333;
}

.result-text {
    font-size: 16px;
    color: #555;
}
</style>
