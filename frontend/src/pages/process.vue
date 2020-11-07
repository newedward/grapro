<template>
  <div id = "home">
    <top-nav></top-nav>
    <el-container height= "100%">
      <el-header>
        <span>我是主流程页</span>
      </el-header>
      <el-container>
        <el-aside width="300px" >
        </el-aside>
        <el-main
          class="infinite-list-wrapper"
          style="overflow:auto">
        </el-main>
      </el-container>
    </el-container>
  </div> 
</template>

<style>

  .el-row {
    margin-bottom: 20px;
    border-radius: 4px;
  }
  .el-roe-title{
    margin-bottom: 20px;
    
  }
  .el-col {
    border-radius: 4px;
  }
  .el-header-home{
    line-height: 40px;
    font-size: 20px;
  }
  .blog{
    background: #EEE ;
    border-radius: 10px;
    margin-bottom: 20px;
  }
  .infinite-list-wrapper{
    height: 100vh;
  }
</style>

<script>
import topNav from '../components/topNav'
  export default {
    name: 'home',
    components: {
      topNav,
    }
  }
</script>
