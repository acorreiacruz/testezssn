<template>
    <div class="mensagem-container">
        <p :class="classe">
            {{msg}}
        </p>
    </div>
</template>

<script>
export default {
    name:"Mensagem",
    props:{
        msg:String,
        classe:String
    }
}
</script>
