<template>
    <thead>
        <tr>
            <th>{{col1}}</th>
            <th>{{col2}}</th>
            <th>{{col3}}</th>
            <th>{{col4}}</th>
            <th>{{col5}}</th>
            <th v-if="col6">{{col6}}</th>
            <th v-if="col7">{{col7}}</th>
        </tr>
    </thead>
</template>

<script>
export default {
    name:"TableHead",
    props:{
        col1:String,
        col2:String,
        col3:String,
        col4:String,
        col5:String,
        col6:String,
        col7:String
    }
}
</script>