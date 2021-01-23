<template>
    <div id = "selectstu">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowTea></flowTea>
      </el-aside>
        <el-main>

        </el-main>
      </el-container>
    </el-container>
    </div>
</template>

<script>
  import topNav from '../components/topNav'
import flowTea from '../components/flowTea'
    export default {
        name: "selectstu",
      components: {
      topNav,
      flowTea,
    },
    }
</script>

<style scoped>

</style>
