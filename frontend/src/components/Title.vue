<template>
    <div class="title-container">
        <h2 class="title"><i :class="fontawesome"></i> {{titulo}}</h2>
    </div>
</template>

<script>
export default {
    name:"Title",
    props:{
        titulo:String,
        fontawesome:String
    }
}
</script>