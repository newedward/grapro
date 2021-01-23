<template>
    <div id = "selectstu">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowTea></flowTea>
      </el-aside>
        <el-main>
          <el-row type="flex"  justify="center" align="middle">
            <el-col :span="12">
            <el-input placeholder="请输入姓名" v-model="selteacher" clearable>
    <el-button slot="append" icon="el-icon-search"></el-button>
  </el-input>
              </el-col>
          </el-row>
          <el-row type="flex" justify="center" v-for="rows in branch">
            <el-card class="teacher" v-for="cols in rows">
              <div slot="header" >
    <span >{{cols.name}}</span>
    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
  </div>
              <el-avatar :size="100" shape="circle" :src="cols.avater"></el-avatar>
              <span class="intro">{{cols.intro}}</span>
        </el-card>
          </el-row>
          <el-row type="flex" justify="center">
          <div class="block">
  <el-pagination
    layout="prev, pager, next"
    :page-count="this.pageNum"
  @prev-click="prePage"
  @next-click="nextPage"
  @current-change="jumpPage">
  </el-pagination>
</div></el-row>
        </el-main>
      </el-container>

    </el-container>
    </div>
</template>

<script>
  import topNav from '../components/topNav'
import flowTea from '../components/flowTea'
    export default {
        name: "selectTea",
      components: {
      topNav,
      flowTea,
    },
      data(){
           return {
           selteacher: '',
             rownumber:4,
           data: [
             {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"张三",intro:"不忘初心"},
            {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"陈斌",intro:"不忘初心"},
            {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"马化腾",intro:"不忘初心"},
            {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"李四",intro:"不忘初心"},
          {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"马云",intro:"不忘初心"},
           ],
             list:[],
             branch:[],
             totalPage: [],
      // 每页显示数量
      pageSize: 12,
      // 共几页
      pageNum: 1,
      // 当前显示的数据
      currentPage: 0
    }
      },
      mounted() {
          this.getpage();
          this.getRow();
      },
      methods:{
          getRow () {
        let arr = [];
        let row = Math.ceil(this.list.length / this.rownumber);
        for (let i = 0; i < row; i++) {
          arr[i] = [];
          let modLast = this.list.length % this.rownumber === 0 ? this.rownumber : this.list.length % this.rownumber;
           let lastRow = i === (row - 1) ? modLast : this.rownumber;
          for (let j = 0; j < lastRow; j++) {
                 arr[i][j] = this.list[this.rownumber * i + j];
          }
         }
        this.branch = arr;
       },
        getpage(){
    for (let i = 0; i < 61; i++) {
      this.data.push({avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"实例",intro:"不忘初心"});
    }
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
      this.getRow();
    },
    // 上一页
    prePage() {
      if (this.currentPage === 0) return ;
      this.list = this.totalPage[--this.currentPage];
      this.getRow();
    },
        jumpPage(val){
            console.log(val);
            this.list = this.totalPage[val-1];
            this.getRow();
        }
      }
    }
</script>

<style scoped>
  .teacher{
  margin: 30px;
}
  .intro{
    font-weight:bold;
	color:#ff9955;
  }
</style>
