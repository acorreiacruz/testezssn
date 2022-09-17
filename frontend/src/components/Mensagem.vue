<template>
    <div class="mensagem-container">
        <p>{{msg}}</p>
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
