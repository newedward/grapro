<template>
  <div id = "home">
    <top-nav></top-nav>
    <el-container height= "100%">
      <el-header>
        <span>我是主流程页</span>
      </el-header>
      <el-container>
        <el-main>
          <div class="block">
  <el-timeline>
    <el-timeline-item timestamp="2020/10/12" placement="top">
      <el-card>
        <h4>题目选择</h4>
        <p>朱振南 选择题目 毕业设计管理系统</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2020/11/25" placement="top">
      <el-card>
        <h4>开题</h4>
        <p>朱振南 完成开题报告 </p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2020/12/2" placement="top">
      <el-card>
        <h4>开题报告修正</h4>
        <p>朱振南 提交于 2020/12/2 20:46</p>
      </el-card>
    </el-timeline-item>
  </el-timeline>
</div>
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
