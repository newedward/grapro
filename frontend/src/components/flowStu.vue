<template>
    <el-menu router="true" >
     <el-menu-item index="/process"><i class="el-icon-star-on">主流程</i></el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-monitor"></i>开题阶段</template>
        <el-menu-item-group>
          <el-menu-item index="/selectTea">导师选择</el-menu-item>
          <el-menu-item index="/startStu">进行开题</el-menu-item>
        </el-menu-item-group>
        <!--<el-submenu index="1-4">-->
          <!--<template slot="title">选项4</template>-->
          <!--<el-menu-item index="1-4-1">选项4-1</el-menu-item>-->
        <!--</el-submenu>-->
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-s-marketing"></i>中期阶段</template>
        <el-menu-item-group>
          <el-menu-item index="/mediumStu">中期提交</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-s-promotion"></i>结题阶段</template>
        <el-menu-item-group>
          <el-menu-item index="/endStu">进行结题</el-menu-item>
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
