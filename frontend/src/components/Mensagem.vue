<template>
    <div class="mensagem-container">
        {{msg}}
    </div>
</template>

<script>
export default {
    name:"Mensagem",
    props:{
        msg:String,
    }
}
</script>
