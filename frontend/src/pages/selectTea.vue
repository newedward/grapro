<template>
    <div id = "selectstu">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowStu></flowStu>
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
    <el-button style="float: right; padding: 3px 0" type="text" @click="apply(cols.uid)">操作按钮</el-button>
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
import flowStu from '../components/flowStu'
    export default {
        name: "selectTea",
      components: {
      topNav,
      flowStu,
    },
      data(){
           return {
           selteacher: '',
             rownumber:4,
           data: [],
          //    {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"张三",intro:"不忘初心"},
          //   {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"陈斌",intro:"不忘初心"},
          //   {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"马化腾",intro:"不忘初心"},
          //   {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"李四",intro:"不忘初心"},
          // {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"马云",intro:"不忘初心"},
             list:[],
             branch:[],
             totalPage: [],
      // 每页显示数量
      pageSize: 12,
      // 共几页
      pageNum: 1,
      // 当前显示的数据
      currentPage: 0,
             watchId:20
    }
      },
    created: function() {
      // this.getcur();
  },
      mounted() {
          this.getdata();
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
        getdata(){
            // for (let i = 0; i < 61; i++) {
    //   this.data.push({avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",name:"实例",intro:"不忘初心"});
    // }
    //从数据库往data中读取数据，但是由于第一期所以首先灌数据，之后再更改
          this.$http.post('/api/getTeacher/',{'userId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {

                      for (var i = 0; i < res1['tealist'].length; i++) {
                        this.data.push({avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                        ,name:res1['ulist'][i]['fields']['name'],intro:res1['tealist'][i]['fields']['requirement']
                        ,uid:res1['ulist'][i]['pk']})
                      }
                      console.log(this.data.length);
                      this.getpage();
                    this.getRow();
                    }
                    else{
                      this.$message.error("获取教师信息失败")
                    }
              })
        },
        getpage(){

    // 根据后台数据的条数和每页显示数量算出一共几页,得0时设为1 ;
    this.pageNum = Math.ceil(this.data.length / this.pageSize) || 1;
          console.log(this.pageNum);
     for (let i = 0; i < this.pageNum; i++) {
      // 每一页都是一个数组 形如 [['第一页的数据'],['第二页的数据'],['第三页数据']]
      // 根据每页显示数量 将后台的数据分割到 每一页,假设pageSize为5， 则第一页是1-5条，即slice(0,5)，第二页是6-10条，即slice(5,10)...
      this.totalPage[i] = this.data.slice(this.pageSize * i, this.pageSize * (i + 1))
    }
    console.log(this.totalPage);
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
        },
        apply(val){
            this.$http.post('/api/applyTeacher/',{'teacherId':val,'studentId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.$message({
                      type: 'info',
                      message: '申请成功'
                        });
                    }
                    else if (res1['err_code']==2){
                      this.$message.error("已经申请过了")
                    }
                    else{
                      this.$message.error("申请失败")
                    }
              })
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
