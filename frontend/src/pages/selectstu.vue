<template>
    <div id = "selectstu">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowTea></flowTea>
      </el-aside>
        <el-main>
          <el-row type="flex" justify="center">
<el-col span="6">
  <el-pagination
    background
    layout="prev, pager, next"
    :page-count="this.pageNum"
  @prev-click="prePage"
  @next-click="nextPage"
  @current-change="jumpPage">
  </el-pagination></el-col>

            <el-button type="primary" icon="el-icon-close" style="float:right">全部拒绝</el-button>

            <el-button type="primary" icon="el-icon-question" style="float:right">全部放入队列</el-button>

</el-row>
          <el-row v-for="item in list">
            <el-card class="student">
              <div slot="header" >
    <span >{{item.code + "-" + item.name}}</span>
    <el-button style="float: right; padding: 3px 0;margin-left:10px;color:#228B22" type="text">同意</el-button>
                <el-button style="float: right; padding: 3px 0;color: #FF0000" type="text">拒绝</el-button>
                <el-button style="float: right; padding: 3px 0" type="text">放入等待队列</el-button>
  </div>
              <el-avatar :size="80" shape="circle" :src="item.avater"></el-avatar>
              <span class="intro">{{item.intro}}</span>
        </el-card>
          </el-row>

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
      data(){
          return {
           data: [
             {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"张三",intro:"不忘初心"},
            {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"陈斌",intro:"不忘初心"},
            {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"马化腾",intro:"不忘初心"},
            {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"李四",intro:"不忘初心"},
          {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"马云",intro:"不忘初心"},
             {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"马云",intro:"不忘初心"},
           ],
            list:[],
            totalPage: [],
      // 每页显示数量
      pageSize: 5,
      // 共几页
      pageNum: 1,
      // 当前显示的数据
      currentPage: 0
    }
      },
      mounted(){
          this.getpage();
      },
      methods:{
          getpage(){
    // 根据后台数据的条数和每页显示数量算出一共几页,得0时设为1 ;
    this.pageNum = Math.ceil(this.data.length / this.pageSize) || 1;
     for (let i = 0; i < this.pageNum; i++) {
      // 每一页都是一个数组 形如 [['第一页的数据'],['第二页的数据'],['第三页数据']]
      // 根据每页显示数量 将后台的数据分割到 每一页,假设pageSize为5， 则第一页是1-5条，即slice(0,5)，第二页是6-10条，即slice(5,10)...
      this.totalPage[i] = this.data.slice(this.pageSize * i, this.pageSize * (i + 1))
    }
   // 获取到数据后显示第一页内容
    this.list = this.totalPage[this.currentPage];
        },
        nextPage() {
      if (this.currentPage === this.pageNum - 1) return ;
      this.list = this.totalPage[++this.currentPage];
    },
    // 上一页
    prePage() {
      if (this.currentPage === 0) return ;
      this.list = this.totalPage[--this.currentPage];
    },
        jumpPage(val){
            console.log(val);
            this.list = this.totalPage[val-1];
        }
      }
    }
</script>

<style scoped>
.student{
  margin:10px;
}
</style>
