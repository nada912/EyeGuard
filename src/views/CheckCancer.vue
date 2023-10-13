<template>
    <div>
        <h1>Check for Eye Cancer</h1>
        <input type="file" @change="onFileChange">
        <button @click="analyzeImage">Analyze Image</button>
        <div v-if="result">
            <h2>Result:</h2>
            <p>{{ result }}</p>
        </div>
    </div>
</template>

<script>
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
            const formData = new FormData()
            formData.append('image', this.image)
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
