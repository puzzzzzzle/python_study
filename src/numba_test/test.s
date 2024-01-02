; ModuleID = 'loop_ba'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc"

@.const.loop_ba = internal constant [8 x i8] c"loop_ba\00"
@_ZN08NumbaEnv8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE = common local_unnamed_addr global i8* null
@".const.missing Environment: _ZN08NumbaEnv8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE" = internal constant [129 x i8] c"missing Environment: _ZN08NumbaEnv8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE\00"
@PyExc_TypeError = external global i8
@".const.can't unbox array from PyObject into native value.  The object maybe of a different type" = internal constant [89 x i8] c"can't unbox array from PyObject into native value.  The object maybe of a different type\00"
@PyExc_RuntimeError = external global i8

; Function Attrs: nofree norecurse nosync nounwind
define i32 @_ZN8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE(i64* noalias nocapture writeonly %retptr, { i8*, i32, i8*, i8*, i32 }** noalias nocapture readnone %excinfo, i8* nocapture readnone %arg.arr.0, i8* nocapture readnone %arg.arr.1, i64 %arg.arr.2, i64 %arg.arr.3, i32* %arg.arr.4, i64 %arg.arr.5.0, i64 %arg.arr.6.0) local_unnamed_addr #0 {
entry:
  %.806 = icmp sgt i64 %arg.arr.5.0, 0
  br i1 %.806, label %B14.lr.ph, label %B28

B14.lr.ph:                                        ; preds = %entry
  %.166.not = icmp eq i64 %arg.arr.5.0, 1
  br i1 %.166.not, label %B28.loopexit17, label %B14.us.us.preheader

B14.us.us.preheader:                              ; preds = %B14.lr.ph
  %n.vec = and i64 %arg.arr.5.0, -32
  br label %B14.us.us

B14.us.us:                                        ; preds = %B14.us.us.preheader, %for.end.loopexit.us-lcssa.us.us.us
  %.31.07.us.us = phi i64 [ %.101.us.us, %for.end.loopexit.us-lcssa.us.us.us ], [ 0, %B14.us.us.preheader ]
  %0 = icmp ult i64 %arg.arr.5.0, 32
  %1 = ptrtoint i32* %arg.arr.4 to i64
  %.92.us.us = mul i64 %.31.07.us.us, %arg.arr.6.0
  %.96.us.us = add i64 %.92.us.us, %1
  %.97.us.us = inttoptr i64 %.96.us.us to i32*
  %.98.us.us = load i32, i32* %.97.us.us, align 4
  br i1 %0, label %for.body.us.us.us.preheader, label %vector.ph

vector.ph:                                        ; preds = %B14.us.us
  %broadcast.splatinsert = insertelement <8 x i32> poison, i32 %.98.us.us, i64 0
  %broadcast.splat = shufflevector <8 x i32> %broadcast.splatinsert, <8 x i32> poison, <8 x i32> zeroinitializer
  %broadcast.splatinsert24 = insertelement <8 x i32> poison, i32 %.98.us.us, i64 0
  %broadcast.splat25 = shufflevector <8 x i32> %broadcast.splatinsert24, <8 x i32> poison, <8 x i32> zeroinitializer
  %broadcast.splatinsert26 = insertelement <8 x i32> poison, i32 %.98.us.us, i64 0
  %broadcast.splat27 = shufflevector <8 x i32> %broadcast.splatinsert26, <8 x i32> poison, <8 x i32> zeroinitializer
  %broadcast.splatinsert28 = insertelement <8 x i32> poison, i32 %.98.us.us, i64 0
  %broadcast.splat29 = shufflevector <8 x i32> %broadcast.splatinsert28, <8 x i32> poison, <8 x i32> zeroinitializer
  br label %vector.body

vector.body:                                      ; preds = %vector.body, %vector.ph
  %index = phi i64 [ 0, %vector.ph ], [ %index.next, %vector.body ]
  %sunkaddr = mul i64 %index, 4
  %2 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr53 = getelementptr i8, i8* %2, i64 %sunkaddr
  %3 = bitcast i8* %sunkaddr53 to <8 x i32>*
  %wide.load = load <8 x i32>, <8 x i32>* %3, align 4
  %sunkaddr54 = mul i64 %index, 4
  %4 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr55 = getelementptr i8, i8* %4, i64 %sunkaddr54
  %sunkaddr56 = getelementptr i8, i8* %sunkaddr55, i64 32
  %5 = bitcast i8* %sunkaddr56 to <8 x i32>*
  %wide.load21 = load <8 x i32>, <8 x i32>* %5, align 4
  %sunkaddr57 = mul i64 %index, 4
  %6 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr58 = getelementptr i8, i8* %6, i64 %sunkaddr57
  %sunkaddr59 = getelementptr i8, i8* %sunkaddr58, i64 64
  %7 = bitcast i8* %sunkaddr59 to <8 x i32>*
  %wide.load22 = load <8 x i32>, <8 x i32>* %7, align 4
  %sunkaddr60 = mul i64 %index, 4
  %8 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr61 = getelementptr i8, i8* %8, i64 %sunkaddr60
  %sunkaddr62 = getelementptr i8, i8* %sunkaddr61, i64 96
  %9 = bitcast i8* %sunkaddr62 to <8 x i32>*
  %wide.load23 = load <8 x i32>, <8 x i32>* %9, align 4
  %10 = add nsw <8 x i32> %wide.load, %broadcast.splat
  %11 = add nsw <8 x i32> %wide.load21, %broadcast.splat25
  %12 = add nsw <8 x i32> %wide.load22, %broadcast.splat27
  %13 = add nsw <8 x i32> %wide.load23, %broadcast.splat29
  %sunkaddr63 = mul i64 %index, 4
  %14 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr64 = getelementptr i8, i8* %14, i64 %sunkaddr63
  %15 = bitcast i8* %sunkaddr64 to <8 x i32>*
  store <8 x i32> %10, <8 x i32>* %15, align 4
  %sunkaddr65 = mul i64 %index, 4
  %16 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr66 = getelementptr i8, i8* %16, i64 %sunkaddr65
  %sunkaddr67 = getelementptr i8, i8* %sunkaddr66, i64 32
  %17 = bitcast i8* %sunkaddr67 to <8 x i32>*
  store <8 x i32> %11, <8 x i32>* %17, align 4
  %sunkaddr68 = mul i64 %index, 4
  %18 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr69 = getelementptr i8, i8* %18, i64 %sunkaddr68
  %sunkaddr70 = getelementptr i8, i8* %sunkaddr69, i64 64
  %19 = bitcast i8* %sunkaddr70 to <8 x i32>*
  store <8 x i32> %12, <8 x i32>* %19, align 4
  %sunkaddr71 = mul i64 %index, 4
  %20 = bitcast i32* %arg.arr.4 to i8*
  %sunkaddr72 = getelementptr i8, i8* %20, i64 %sunkaddr71
  %sunkaddr73 = getelementptr i8, i8* %sunkaddr72, i64 96
  %21 = bitcast i8* %sunkaddr73 to <8 x i32>*
  store <8 x i32> %13, <8 x i32>* %21, align 4
  %index.next = add nuw i64 %index, 32
  %22 = icmp eq i64 %n.vec, %index.next
  br i1 %22, label %middle.block, label %vector.body, !llvm.loop !0

middle.block:                                     ; preds = %vector.body
  %23 = icmp eq i64 %n.vec, %arg.arr.5.0
  br i1 %23, label %for.end.loopexit.us-lcssa.us.us.us, label %for.body.us.us.us.preheader

for.body.us.us.us.preheader:                      ; preds = %B14.us.us, %middle.block
  %loop.index3.us.us.us.ph = phi i64 [ 0, %B14.us.us ], [ %n.vec, %middle.block ]
  br label %for.body.us.us.us

for.end.loopexit.us-lcssa.us.us.us:               ; preds = %for.body.us.us.us, %middle.block
  %.101.us.us = add nuw nsw i64 %.31.07.us.us, 1
  %exitcond18.not = icmp eq i64 %.101.us.us, %arg.arr.5.0
  br i1 %exitcond18.not, label %B28, label %B14.us.us

for.body.us.us.us:                                ; preds = %for.body.us.us.us.preheader, %for.body.us.us.us
  %loop.index3.us.us.us = phi i64 [ %.180.us.us.us, %for.body.us.us.us ], [ %loop.index3.us.us.us.ph, %for.body.us.us.us.preheader ]
  %scevgep52 = getelementptr i32, i32* %arg.arr.4, i64 %loop.index3.us.us.us
  %.174.us.us.us = load i32, i32* %scevgep52, align 4
  %.175.us.us.us = add nsw i32 %.174.us.us.us, %.98.us.us
  store i32 %.175.us.us.us, i32* %scevgep52, align 4
  %.180.us.us.us = add nuw nsw i64 %loop.index3.us.us.us, 1
  %exitcond.not = icmp eq i64 %arg.arr.5.0, %.180.us.us.us
  br i1 %exitcond.not, label %for.end.loopexit.us-lcssa.us.us.us, label %for.body.us.us.us, !llvm.loop !2

B28.loopexit17:                                   ; preds = %B14.lr.ph
  %.98.us.pre = load i32, i32* %arg.arr.4, align 4
  %.175.us11 = shl nsw i32 %.98.us.pre, 1
  store i32 %.175.us11, i32* %arg.arr.4, align 4
  br label %B28

B28:                                              ; preds = %for.end.loopexit.us-lcssa.us.us.us, %B28.loopexit17, %entry
  store i64 0, i64* %retptr, align 8
  ret i32 0
}

define i8* @_ZN7cpython8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE(i8* nocapture readnone %py_closure, i8* %py_args, i8* nocapture readnone %py_kws) local_unnamed_addr {
entry:
  %.5 = alloca i8*, align 8
  %.6 = call i32 (i8*, i8*, i64, i64, ...) @PyArg_UnpackTuple(i8* %py_args, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.const.loop_ba, i64 0, i64 0), i64 1, i64 1, i8** nonnull %.5)
  %.7 = icmp eq i32 %.6, 0
  %.21 = alloca { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }, align 8
  %.43 = alloca i64, align 8
  br i1 %.7, label %common.ret, label %entry.endif, !prof !4

common.ret:                                       ; preds = %entry.endif.endif.endif.thread, %entry, %entry.endif.endif.endif.endif, %entry.endif.if
  %common.ret.op = phi i8* [ null, %entry.endif.if ], [ %.69, %entry.endif.endif.endif.endif ], [ null, %entry ], [ null, %entry.endif.endif.endif.thread ]
  ret i8* %common.ret.op

entry.endif:                                      ; preds = %entry
  %.11 = load i8*, i8** @_ZN08NumbaEnv8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE, align 8
  %.16 = icmp eq i8* %.11, null
  br i1 %.16, label %entry.endif.if, label %entry.endif.endif, !prof !4

entry.endif.if:                                   ; preds = %entry.endif
  call void @PyErr_SetString(i8* nonnull @PyExc_RuntimeError, i8* getelementptr inbounds ([129 x i8], [129 x i8]* @".const.missing Environment: _ZN08NumbaEnv8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE", i64 0, i64 0))
  br label %common.ret

entry.endif.endif:                                ; preds = %entry.endif
  %.20 = load i8*, i8** %.5, align 8
  %.24 = bitcast { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }* %.21 to i8*
  %0 = bitcast { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }* %.21 to i8*
  call void @llvm.memset.p0i8.i64(i8* noundef nonnull align 8 dereferenceable(56) %0, i8 0, i64 56, i1 false)
  %.25 = call i32 @NRT_adapt_ndarray_from_python(i8* %.20, i8* nonnull %.24)
  %1 = bitcast { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }* %.21 to i8*
  %sunkaddr = getelementptr inbounds i8, i8* %1, i64 24
  %2 = bitcast i8* %sunkaddr to i64*
  %.29 = load i64, i64* %2, align 8
  %.30 = icmp ne i64 %.29, 4
  %.31 = icmp ne i32 %.25, 0
  %.32 = or i1 %.31, %.30
  br i1 %.32, label %entry.endif.endif.endif.thread, label %entry.endif.endif.endif.endif, !prof !4

entry.endif.endif.endif.thread:                   ; preds = %entry.endif.endif
  call void @PyErr_SetString(i8* nonnull @PyExc_TypeError, i8* getelementptr inbounds ([89 x i8], [89 x i8]* @".const.can't unbox array from PyObject into native value.  The object maybe of a different type", i64 0, i64 0))
  br label %common.ret

entry.endif.endif.endif.endif:                    ; preds = %entry.endif.endif
  %3 = bitcast { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }* %.21 to i8**
  %.36.fca.0.load = load i8*, i8** %3, align 8
  %4 = bitcast { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }* %.21 to i8*
  %sunkaddr3 = getelementptr inbounds i8, i8* %4, i64 32
  %5 = bitcast i8* %sunkaddr3 to i32**
  %.36.fca.4.load = load i32*, i32** %5, align 8
  %6 = bitcast { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }* %.21 to i8*
  %sunkaddr4 = getelementptr inbounds i8, i8* %6, i64 40
  %7 = bitcast i8* %sunkaddr4 to i64*
  %.36.fca.5.0.load = load i64, i64* %7, align 8
  %8 = bitcast { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] }* %.21 to i8*
  %sunkaddr5 = getelementptr inbounds i8, i8* %8, i64 48
  %9 = bitcast i8* %sunkaddr5 to i64*
  %.36.fca.6.0.load = load i64, i64* %9, align 8
  store i64 0, i64* %.43, align 8
  %.49 = call i32 @_ZN8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE(i64* nonnull %.43, { i8*, i32, i8*, i8*, i32 }** nonnull undef, i8* undef, i8* undef, i64 undef, i64 undef, i32* %.36.fca.4.load, i64 %.36.fca.5.0.load, i64 %.36.fca.6.0.load) #1
  call void @NRT_decref(i8* %.36.fca.0.load)
  %.69 = call i8* @PyLong_FromLongLong(i64 0)
  br label %common.ret
}

declare i32 @PyArg_UnpackTuple(i8*, i8*, i64, i64, ...) local_unnamed_addr

declare void @PyErr_SetString(i8*, i8*) local_unnamed_addr

declare i32 @NRT_adapt_ndarray_from_python(i8* nocapture, i8* nocapture) local_unnamed_addr

declare i8* @PyLong_FromLongLong(i64) local_unnamed_addr

; Function Attrs: nofree norecurse nosync nounwind
define i64 @cfunc._ZN8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE({ i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] } %.1) local_unnamed_addr #0 {
entry:
  %.3 = alloca i64, align 8
  store i64 0, i64* %.3, align 8
  %extracted.data = extractvalue { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] } %.1, 4
  %extracted.shape = extractvalue { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] } %.1, 5
  %.7 = extractvalue [1 x i64] %extracted.shape, 0
  %extracted.strides = extractvalue { i8*, i8*, i64, i64, i32*, [1 x i64], [1 x i64] } %.1, 6
  %.8 = extractvalue [1 x i64] %extracted.strides, 0
  %.9 = call i32 @_ZN8__main__7loop_baB2v1B38c8tJTIcFKzyF2ILShI4CrgQElQb6HczSBAA_3dE5ArrayIiLi1E1C7mutable7alignedE(i64* nonnull %.3, { i8*, i32, i8*, i8*, i32 }** nonnull undef, i8* undef, i8* undef, i64 undef, i64 undef, i32* %extracted.data, i64 %.7, i64 %.8) #1
  %.19 = load i64, i64* %.3, align 8
  ret i64 %.19
}

; Function Attrs: noinline
define linkonce_odr void @NRT_decref(i8* %.1) local_unnamed_addr #1 {
.3:
  %.4 = icmp eq i8* %.1, null
  br i1 %.4, label %common.ret1, label %.3.endif, !prof !4

common.ret1:                                      ; preds = %.3, %.3.endif
  ret void

.3.endif:                                         ; preds = %.3
  fence release
  %.8 = bitcast i8* %.1 to i64*
  %.4.i = atomicrmw sub i64* %.8, i64 1 monotonic, align 8
  %.10 = icmp eq i64 %.4.i, 1
  br i1 %.10, label %.3.endif.if, label %common.ret1, !prof !4

.3.endif.if:                                      ; preds = %.3.endif
  fence acquire
  tail call void @NRT_MemInfo_call_dtor(i8* nonnull %.1)
  ret void
}

declare void @NRT_MemInfo_call_dtor(i8*) local_unnamed_addr

; Function Attrs: argmemonly nofree nounwind willreturn writeonly
declare void @llvm.memset.p0i8.i64(i8* nocapture writeonly, i8, i64, i1 immarg) #2

attributes #0 = { nofree norecurse nosync nounwind }
attributes #1 = { noinline }
attributes #2 = { argmemonly nofree nounwind willreturn writeonly }

!0 = distinct !{!0, !1}
!1 = !{!"llvm.loop.isvectorized", i32 1}
!2 = distinct !{!2, !3, !1}
!3 = !{!"llvm.loop.unroll.runtime.disable"}
!4 = !{!"branch_weights", i32 1, i32 99}
