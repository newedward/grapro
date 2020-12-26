<template>
    <el-menu >
     <el-menu-item index="1-1"><i class="el-icon-star-on">主流程</i></el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-monitor"></i>开题阶段</template>
        <el-menu-item-group>
          <el-menu-item index="1-1">导师选择</el-menu-item>
          <el-menu-item index="1-2">题目选择</el-menu-item>
          <el-menu-item index="1-3">进行开题</el-menu-item>
        </el-menu-item-group>
        <!--<el-submenu index="1-4">-->
          <!--<template slot="title">选项4</template>-->
          <!--<el-menu-item index="1-4-1">选项4-1</el-menu-item>-->
        <!--</el-submenu>-->
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-s-marketing"></i>中期阶段</template>
        <el-menu-item-group>
          <el-menu-item index="2-1">进度汇报</el-menu-item>
          <el-menu-item index="2-2">中期提交</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-s-promotion"></i>结题阶段</template>
        <el-menu-item-group>
          <el-menu-item index="3-1">项目提交</el-menu-item>
          <el-menu-item index="1-2">题目选择</el-menu-item>
          <el-menu-item index="1-3">进行开题</el-menu-item>
        </el-menu-item-group>

      </el-submenu>
    </el-menu>
</template>

<script>
    export default {
        name: "flowStu"
    }
</script>

<style scoped>

</style>
